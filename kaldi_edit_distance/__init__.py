from . import edit_distance as ed


def _get_ele(seq1, seq2):
    seq1 = list(seq1)
    seq2 = list(seq2)

    if len(seq1) == len(seq2) == 0:
        return 0
    first_ele = (seq1 + seq2)[0]
    if any(not isinstance(v, type(first_ele)) for v in (seq1 + seq2)):
        raise ValueError(
            'All types of elements in seq1 and seq2 should be same')
    return first_ele


def levenshtein_edit_distance(seq1, seq2, details=False):
    ele = _get_ele(seq1, seq2)

    if isinstance(ele, int):
        if details:
            return ed.levenshtein_edit_distance_detail_int(seq1, seq2)
        else:
            return ed.levenshtein_edit_distance_int(seq1, seq2)
    if isinstance(ele, float):
        if details:
            return ed.levenshtein_edit_distance_detail_float(seq1, seq2)
        else:
            return ed.levenshtein_edit_distance_float(seq1, seq2)
    if isinstance(ele, (str, bytes)):
        if isinstance(ele, str):
            seq1 = [i.encode() for i in seq1]
            seq2 = [i.encode() for i in seq2]
        if details:
            return ed.levenshtein_edit_distance_detail_bytes(seq1, seq2)
        else:
            return ed.levenshtein_edit_distance_bytes(seq1, seq2)
    else:
        raise ValueError(
            'Not supported type: {}'.format(type(ele)))


def levenshtein_alignment(seq1, seq2, eps_symbol):
    ele = _get_ele(seq1, seq2)
    if not isinstance(eps_symbol, type(ele)):
        raise TypeError('eps_symbol must have {} type'.format(type(ele)))

    if isinstance(ele, int):
        total, output = ed.levenshtein_alignment_int(seq1, seq2, eps_symbol)

    elif isinstance(ele, float):
        total, output = ed.levenshtein_alignment_float(seq1, seq2, eps_symbol)
    if isinstance(ele, (str, bytes)):
        if isinstance(ele, str):
            seq1 = [i.encode() for i in seq1]
            seq2 = [i.encode() for i in seq2]
            eps_symbol = eps_symbol.encode()
        total, output = ed.levenshtein_alignment_bytes(seq1, seq2, eps_symbol)
    else:
        raise ValueError(
            'Not supported type: {}'.format(type(ele)))
    rseq1 = [v1 for v1, v2 in output]
    rseq2 = [v2 for v1, v2 in output]
    if isinstance(ele, str):
        rseq1 = [i.decode() for i in rseq1]
        rseq2 = [i.decode() for i in rseq2]
    return total, rseq1, rseq2
