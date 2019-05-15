# NL1DP-PY

Data-preprocessing tool for NLP

<p align="center">
  <a href="#"><img src="./misc/alysfabienne_verdier.png" /></a>
</p>

Paint by [Fabienne Verdier](https://fabienneverdier.com/)

## Installation

```bash
$ pip install https://github.com/tlentali/NL1DP-PY
```

## Usage

```python
in process
```

## Feature

| Feature                       | type   | description                                                   |
| :---------------------------: | :----: | :-----------------------------------------------------------: |
| clean_text                    | string | remove symbols other than letter, number and punctuation      |
| clean_numbers                 | string | replace numbers by '#'                                        |
| replace_typical_misspell      | string | correct usual misspelling from a dict in ```config.py```      |
| smart_space                   | string | remove redondant space                                        |
| to_lower                      | string | lower case the text                                           |
| formating_caracter_correction | string | replace special character to basic character, like 'œ' to 'oe'|
| remove_repeated_punctuation   | string | replace repeated punctuation by a word                        |
| count_lower                   | int    | count lower case character                                    |
| count_upper                   | int    | count upper case character                                    |
| count_punctuation             | dict   | count each different punctuation and symbol                   |