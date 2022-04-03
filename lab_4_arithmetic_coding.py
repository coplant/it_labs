from decimal import Decimal
from collections import Counter
import math

class ArithmeticEncoding:
    def __init__(self, message):
        self.message = message
        self.length = len(message)
        self.frequency_table = self.get_frequency_table(message)
        self.probability_table = self.get_probability_table(self.frequency_table)

    @staticmethod
    def get_frequency_table(message):
        frequency_table = Counter(message)
        return frequency_table

    @staticmethod
    def get_probability_table(frequency_table):
        total_frequency = sum(list(frequency_table.values()))
        probability_table = {}
        for key, value in frequency_table.items():
            probability_table[key] = value / total_frequency
        return probability_table

    @staticmethod
    def get_encoded_value(encoder):
        last_stage = list(encoder[-1].values())
        last_stage_values = []
        for sublist in last_stage:
            for element in sublist:
                last_stage_values.append(element)
        last_stage_min = min(last_stage_values)
        last_stage_max = max(last_stage_values)
        return (last_stage_min + last_stage_max) / 2

    @staticmethod
    def process_stage(probability_table, stage_min, stage_max):
        stage_probs = {}
        stage_domain = stage_max - stage_min
        for term_idx in range(len(probability_table.items())):
            term = list(probability_table.keys())[term_idx]
            term_prob = Decimal(probability_table[term])
            cum_prob = term_prob * stage_domain + stage_min
            stage_probs[term] = [stage_min, cum_prob]
            stage_min = cum_prob
        return stage_probs

    def get_entropy(self):
        return -sum([p * math.log(p) / math.log(2.0) for k, p in self.probability_table.items()])

    def encode(self):
        encoder = []
        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)
        for msg_term_idx in range(len(self.message)):
            stage_probs = self.process_stage(self.probability_table, stage_min, stage_max)
            msg_term = self.message[msg_term_idx]
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]
            encoder.append(stage_probs)
        stage_probs = self.process_stage(self.probability_table, stage_min, stage_max)
        encoder.append(stage_probs)
        encoded_msg = self.get_encoded_value(encoder)
        return encoder, encoded_msg

    def decode(self):
        decoder = []
        decoded_msg = ""
        stage_min = Decimal(0.0)
        stage_max = Decimal(1.0)
        for idx in range(self.length):
            stage_probs = self.process_stage(self.probability_table, stage_min, stage_max)
            for msg_term, value in stage_probs.items():
                if value[0] <= Decimal(self.encode()[1]) <= value[1]:
                    break
            decoded_msg = decoded_msg + msg_term
            stage_min = stage_probs[msg_term][0]
            stage_max = stage_probs[msg_term][1]
            decoder.append(stage_probs)
        stage_probs = self.process_stage(self.probability_table, stage_min, stage_max)
        decoder.append(stage_probs)
        return decoder, decoded_msg


def main():
    message = input("Enter message: ")
    ae = ArithmeticEncoding(message)
    print(f"Entropy: {ae.get_entropy()}")
    print(f"Encoded: {ae.encode()[1]}")
    print(f"Decoded: {ae.decode()[1]}")


if __name__ == '__main__':
    main()
