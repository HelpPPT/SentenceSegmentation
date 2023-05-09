import itertools

from kss import split_sentences as kss_split_sentences


def split_sentences(sentences: list[str]) -> list[str]:
    kss_split_result: list[list[str]] = kss_split_sentences(sentences)
    return list(itertools.chain(*kss_split_result))


if __name__ == '__main__':
    a = split_sentences([
        "트리(Tree)의 개념 트리는 노드로 이루어진 자료구조로 스택이나 큐와 같은 선형 구조가 아닌 비선형 자료구조이다. 트리는 계층적 관계를 표현하는 자료구조이다.",
        "트리(Tree)의 개념 트리는 노드로 이루어진 자료구조로 스택이나 큐와 같은 선형 구조가 아닌 비선형 자료구조이다. 트리는 계층적 관계를 표현하는 자료구조이다."
    ])
    print(a)
