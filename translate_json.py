import json
from pathlib import Path
from copy import deepcopy
import pickle
from textblob import TextBlob
import textblob

def load_json(file: str) -> dict:
    """
    """
    with open(file, 'r', encoding='utf-8') as fin:
        try:
            json_file = json.load(fin)
        except json.JSONDecodeError:
            with open(file, 'r', encoding='utf-8-sig') as sfin:
                json_file = json.load(sfin)
    return json_file

class FileTranslator:
    """
    """
    def __init__(self, file: str):
        """
        """
        if Path(file).suffix == '.json':
            self.file_name = Path(file).name
            self.file_path = Path(file)
            self.file = file
        self.rows = []
        self.translation_file = None
        if Path(file).suffix == '.pik':
            self.translation_file = file
            self.file = str(Path(Path(self.translation_file).parent, 
                            Path(self.translation_file).stem))
            self.file_path = Path(file)
            self.file_name = self.file_path.name
        self.json = load_json(self.file)
        self.data = None
        self.translated_json = None
        self.__load_contents()
    
    def __load_contents(self):
        """
        """
        if self.translation_file:
            print(self.translation_file)
            with open(self.translation_file, 'rb') as trans_file:
                self.rows = pickle.load(trans_file, encoding='utf-8')
            self.data = self.json['data']
            self.translated_json = deepcopy(self.json)
        else:
            self.data = self.json['data']
            self.translated_json = deepcopy(self.json)
            for row in self.data:
                contents = Contents(row[0][0], str(row[1][0]))
                self.rows.append(contents)
            self.translation_file = Path(str(self.file_path) + '.pik')
            
            with open(self.translation_file, 'wb') as trans_file:
                pickle.dump(self.rows, trans_file)

    def cleanup_translation(self):
        """
        """
        for row, translated_row in zip(self.rows, self.translated_json['data']):
            target = ''
            for segment in row.segments:
                target += segment.target
            try:
                target = int(target)
            except ValueError:
                pass
            translated_row[1][0] = target
        new_json = Path(self.file_path.parent, f'{self.file_path.stem}_es-ES{self.file_path.suffix}')
        with open(new_json, 'w', encoding='utf-8-sig') as fout:
            json.dump(self.translated_json, fout, ensure_ascii=False)
    
    def save_changes(self):
        """
        """
        with open(self.translation_file, 'wb') as trans_file:
            pickle.dump(self.rows, trans_file)

class Contents:
    """
    """
    def __init__(self, key: str, value: str):
        """
        """
        self.key = key
        self.segments = []
        self.__load_segments(value)
    
    def __load_segments(self, value: str):
        """
        """
        text = TextBlob(value)
        sentences = text.sentences
        for idx, sentence in enumerate(sentences):
            self.segments.append(Segment(idx, sentence))


class Segment:
    """
    """
    def __init__(self, idx: int, source: str):
        """
        """
        self.__generate_segment(source)
        self.id = idx
    
    def __generate_segment(self, source: str):
        """
        """
        self.source = source.string
        self.source_sentence = source
        try:
            self.target = source.translate(to='es').string
        except textblob.exceptions.NotTranslated:
            self.target = ''

if __name__ == '__main__':
    """
    """
    file = r'd:\PyProjects\gon_json\files\TET_Aviary Attorney\package\1catendcutscene.json'
    file = r'd:\PyProjects\gon_json\files\TET_Aviary Attorney\package\1catintro.json'
    f= FileTranslator(file)
    #f.load_contents()
    with open(f.translation_file, 'rb') as trans_file:
        print(pickle.load(trans_file))
    for row in f.rows:
        for segment in row.segments:
            print(segment.source, segment.target)
    f.cleanup_translation()
