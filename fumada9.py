import numpy as np
import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

# Cargar el modelo GPT-3 preentrenado
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.add_special_tokens({'pad_token': '[PAD]'})  # Agregar token de padding
model = TFGPT2LMHeadModel.from_pretrained("gpt2")


# Generar datos de entrenamiento de ejemplo
num_samples = 1000
sequences = []  # Lista de secuencias temporales de matrices de transición

for _ in range(num_samples):
    # Generar una matriz de transición de muestra
    transition_matrix = np.random.rand(5, 5)
    transition_matrix = transition_matrix / np.sum(transition_matrix, axis=1, keepdims=True)  # Asegurar que las filas sumen uno
    sequences.append(transition_matrix)

# Convertir las secuencias en texto para el modelo GPT-3
text_sequences = ["\n".join(["\t".join([str(value) for value in row]) for row in sequence]) for sequence in sequences]

# Tokenizar las secuencias
input_ids = tokenizer(text_sequences, truncation=True, padding=True, max_length=100, return_tensors="tf").input_ids


# Entrenar el modelo GPT-3 para completar la secuencia siguiente
model.compile(optimizer="adam", loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

model.fit(x=input_ids[:, :-1], y=input_ids[:, 1:], batch_size=32, epochs=10)

# Utilizar el modelo para hacer predicciones
# Supongamos que tenemos una matriz de transición de prueba
test_sequence = np.random.rand(5, 5)
test_sequence = test_sequence / np.sum(test_sequence, axis=1, keepdims=True)  # Asegurar que las filas sumen uno

test_text_sequence = "\n".join(["\t".join([str(value) for value in row]) for row in test_sequence])
input_ids = tokenizer.encode(test_text_sequence, return_tensors="tf")

predicted_sequence = model.generate(input_ids, max_length=36, num_return_sequences=1)

# Decodificar la secuencia generada
predicted_text_sequence = tokenizer.decode(predicted_sequence[0], skip_special_tokens=True)
predicted_matrix = np.array([[float(value) for value in row.split("\t")] for row in predicted_text_sequence.split("\n")])

print("Entrada:")
print(test_sequence)
print("Predicción:")
print(predicted_matrix)
