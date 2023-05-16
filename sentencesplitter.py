import itertools
from typing import List

from kss import split_sentences as kss_split_sentences


def split_sentences(sentences: List[str]) -> List[str]:
    kss_split_result: List[List[str]] = kss_split_sentences(sentences)
    return list(itertools.chain(*kss_split_result))


if __name__ == '__main__':
    a = split_sentences([
        "대법원장과 대법관이 아닌 법관의 임기는 10년으로 하며, 법률이 정하는 바에 의하여 연임할 수 있다."
        " 대통령은 국회에 출석하여 발언하거나 서한으로 의견을 표시할 수 있다. 대통령은 헌법과 법률이 정하는 바에 의하여 공무원을 임면한다."
        " 대한민국의 국민이 되는 요건은 법률로 정한다. 모든 국민은 능력에 따라 균등하게 교육을 받을 권리를 가진다."
        " 교육의 자주성·전문성·정치적 중립성 및 대학의 자율성은 법률이 정하는 바에 의하여 보장된다."
        " 국무총리·국무위원 또는 정부위원은 국회나 그 위원회에 출석하여 국정처리상황을 보고하거나 의견을 진술하고 질문에 응답할 수 있다."
        " 이 헌법중 공무원의 임기 또는 중임제한에 관한 규정은 이 헌법에 의하여 그 공무원이 최초로 선출 또는 임명된 때로부터 적용한다."
        " 국가는 균형있는 국민경제의 성장 및 안정과 적정한 소득의 분배를 유지하고, 시장의 지배와 경제력의 남용을 방지하며,"
        " 경제주체간의 조화를 통한 경제의 민주화를 위하여 경제에 관한 규제와 조정을 할 수 있다.",
        "트리(Tree)의 개념 트리는 노드로 이루어진 자료구조로 스택이나 큐와 같은 선형 구조가 아닌 비선형 자료구조이다. 트리는 계층적 관계를 표현하는 자료구조이다."
    ])
    print(a)
