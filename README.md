# RapTextGeneratorRNN
Dieses einfache Rekurrentes Neuronales Netz wird mit einem Datensatz von Raptexten gefüttert und sollte dann diese Generieren.


# Generelle Informationen
Als Basis wurde folgendes RNN genutzt von Tensorflow: <br>
https://www.tensorflow.org/text/tutorials/text_generation

<b>Hinzugefügt wurde:</b>
- Hyperparameter Optimization
- Checkpoint Saving (Saving Best/ Saving each weight)
- Early Stopping

Das Netz wurde in mit einem 130k Lines Datenset bestehend aus Raptexten gefüttert:  <br>
https://www.kaggle.com/datasets/ngxdtv/deutsche-rap-texte


Nach Optimierung habe ich mich für folgende Hyper Parameter entschieden: <br>
{'embedding_dim': 512, 'rnn_units': 1024, 'batch_size': 128, 'buffer_size': 20000, 'learning_rate': 0.1}


# Generierte Texte:
<b>(Nach etwa 12 Minuten trainieren, loss = 1.3362)</b>

[Part 1]
Tausend Untergloubet wieder beote misslich steekn <br>
Auch was zu miesin Süxerschmetten dass ich nur rein nde [?] weitsavie<br>
Allut wern ich auf erlebt is seinem Lame wo jungs - -ma ja<br>
(Samy ie Phai ne ente<br>
Kolles fick cutte auf hamburg... Cath der Strope á an ihn Supersetziert kamalen<br>
Cocko cana pa brauba whass zu flews<br>
Wir nicht ins Hypen quicks das ich passt mir Ering von wighollablande steibe liebt zu<br>
Mam gehst wie ein Beingängerfriun sie den Hood ist geens raps (du Chacks and ge in ne Kiss und Wir sind es Gesega<br>
Privettenkentylich wie heiß die ‘ne Cane<br>
Sag wie sie eine Hammung und siehst dichen Covas<br>
Simhst es man rausbu-du bist nur auch immer so gellow)<br>
?... sagen er gehen was ich grad Oh<br>
Dies geht mit dem Samy Deluxe<br>
