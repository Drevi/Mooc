# Write your solution here

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

in_layers = int(input("Layers: "))

layers = []

for i in range(0, in_layers):
    right = letters[i] * i + letters[i+1:in_layers]
    left = right[::-1]
    layer = left + letters[i] + right
    layers.append(layer)

for i in range(len(layers)-1, 0, -1):
    print(layers[i])

for i in range(0, len(layers)):
    print(layers[i])



    