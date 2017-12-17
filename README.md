# python kaldi edit distance
python wrappers of the edit_distance functions of Kaldi-ASR: https://github.com/kaldi-asr/kaldi/

## Usage
```python
>>> import kaldi_edit_distance as ked
>>> ked.levenshtein_edit_distance([1,2,3], [0,1,1,2,0,3])
3
>>> ked.levenshtein_edit_distance([1,2,3], [0,1,1,2,0,3], detail=True)
ErrorStats(total_cost=4, ins_num=3, del_num=0, sub_num=1)
>>> total, aligned1, aligned2 = ked.levenshtein_alignment([1,2,3], [0,1,1,2,0,3], -1)
>>> total, aligned1, aligned2
(3, [-1, -1, 1, 2, -1, 3], [0, 1, 1, 2, 0, 3])
```

## TODO
- Add test codes
