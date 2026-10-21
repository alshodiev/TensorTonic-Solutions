class SimpleTokenizer:
    def __init__(self):
        self.word_to_id = {}
        self.id_to_word = {}
        self.vocab_size = 0
        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: list[str]) -> None:
        """
        Builds the vocabulary in place.
        
        i: texts
        o: Dict
        """
        self.word_to_id = {self.pad_token : 0,
                self.unk_token: 1,
                self.bos_token: 2,
                self.eos_token: 3
        }
        lst_texts = set()
        for text in texts:
            text = text.lower().strip().split()
            lst_texts.update(set(text))
        sorted_lst = sorted(lst_texts)
        
        for i in range(len(sorted_lst)):
            self.word_to_id[sorted_lst[i]] = i + 4

        self.vocab_size = len(self.word_to_id)

        self.id_to_word = {v: k for k,v in self.word_to_id.items()}
        
    def encode(self, text: str) -> list[int]:
        """
        Returns token IDs for the input text.

        i: text str
        o: token id list
        """
        text = text.lower().strip().split()
        out = []
        for t in text:
            if t in self.word_to_id:
                out.append(self.word_to_id[t])
            else:
                out.append(1)
        return out
        
    def decode(self, ids: list[int]) -> str:
        """
        Returns the decoded, space-separated text.

        i: token id list
        o: text str
        """
        out = []
        for id in ids:
            if id in self.id_to_word:
                out.append(self.id_to_word[id])
            else:
                out.append(self.unk_token)
        out_text = " ".join(out)
        return out_text
                
        