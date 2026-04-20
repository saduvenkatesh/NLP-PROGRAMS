import torch
import torch.nn as nn

class LSTM(nn.Module):
    def __init__(self, vocab_size, embed_size, hidden_size, output_size):
        super(LSTM, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.embedding(x)
        output, (hidden, cell) = self.lstm(x)
        out = self.fc(hidden[-1])
        return out

model = LSTM(5000, 128, 64, 2)
print(model)