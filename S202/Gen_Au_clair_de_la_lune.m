% Définir les fréquences des notes dans la gamme tempérée occidentale
notes = {'Re2', 'Mi2', 'Fa2', 'Sol2', 'La2', 'Si2', 'Do3', 'Re3', 'Mi3'};
frequence_notes = [147, 165, 175, 196, 220, 247, 262, 294, 330];

% Définir le morceau de musique et les durées
morceau = {'Do3', 'Do3', 'Do3', 'Re3', 'Mi3', 'Re3', 'Do3', 'Mi3', 'Re3', 'Re3', 'Do3', 'Do3', 'Do3', 'Do3', 'Re3', 'Mi3', 'Re3', 'Re3', 'Mi3', 'Re3', 'Re3', 'Do3', 'Re3', 'Re3', 'Re3', 'Re3', 'La2', 'La2', 'Re3', 'Do3', 'Si2', 'La2', 'Sol2', 'Do3', 'Do3', 'Do3', 'Re3', 'Mi3', 'Re3', 'Do3', 'Mi3', 'Re3', 'Re3', 'Do3'}; 
durees = [1/2, 1/2, 1/2, 1/2, 1, 1, 1/2, 1/2, 1/2, 1/2, 2, 1/2, 1/2, 1/2, 1/2, 1, 1, 1/2, 1/2, 1/2, 1/2, 2, 1/2, 1/2, 1/2, 1/2, 1, 1, 1/2, 1/2, 1/2, 1/2, 2, 1/2, 1/2, 1/2, 1/2, 1, 1, 1/2, 1/2, 1/2, 1/2, 2];

% Définir les paramètres du signal
Fs = 8000; % Fréquence d'échantillonnage
T = 1/Fs; % Période d'échantillonnage

% Créer le signal pour chaque note et jouer le morceau
signal_morceau = [];
for i = 1:length(morceau)
    L = Fs * durees(i); % Longueur du signal basée sur la durée de la note
    t = (0:L-1)*T; % Échelle de temps
    F = frequence_notes(strcmp(notes, morceau{i})); % Trouver la fréquence de la note
    A = 0.5; % Amplitude de la note
    note = A*sin(2*pi*F*t); % Signal de la note
    silence = zeros(1, Fs/32); % Silence après chaque note
    signal_morceau = [signal_morceau note silence]; % Ajouter la note et le silence au morceau
end

% Jouer le morceau
sound(signal_morceau, Fs);

% Enregistrer le morceau en fichier .wav
audiowrite('morceau.wav', signal_morceau, Fs);