# 대한민국 공군 합격 예측 프로그램  ROKAF Admission Probability Calculator

이 프로그램은 대한민국 공군의 합격 가능성을 예측할 수 있는 파이썬 기반 프로그램입니다. 사용자로부터 필요한 점수를 입력받아 최종 점수와 커트라인 점수를 계산하여 결과를 제공합니다.

![ROKAFlogo](https://i.namu.wiki/i/WoiNEG6LXg5epIwmNnH41OUFaW2JCP_BvsGZimQ1BQgnleXEseGKmGuAdlTZ0OG_JrnS_J4ztvLu-gnNPfhRBw.svg)

## 기능

- 사용자가 입력한 점수를 기반으로 합격 여부 예측
- 입력된 점수에 대한 유효성 검사
- 시뮬레이션을 통한 점수 커트라인 계산
- 합격 여부에 따른 메시지 표시 

## 사용 방법

1. **프로그램 실행**: 파이썬 환경에서 프로그램을 실행합니다.
2. **점수 입력**: 프로그램이 요구하는 대로 본인의 점수를 입력합니다.
3. **결과 확인**: 입력한 점수에 따라 합격 여부가 표시됩니다.

## 유효성 검사

- 각각 입력해야 하는 값에 따라 지정된 범위 내의 값을 표기해야 합니다.
- 숫자만 입력 가능합니다.
- 잘못된 입력이 있을 경우 경고 메시지를 표시합니다. 

## 커트라인 설정

- 모집인원과 지원자수에 따라 다르게 설정되며, 특정 확률에 따라 랜덤으로 설정됩니다.
- 모집인원이 많거나 지원자수가 적다면 커트라인이 낮아지는 경향이 있고 아니라면 일반적으로 높아지는 경향이 있습니다.
- 지원자수만큼의 점수가 랜덤하게 생성되므로(이때 가장 많이 분포하고 있는 점수대에는 가중치를 둬 이 점수대에 점수가 뜰 확률이 높아집니다) 실행시마다 조금씩 결과가 달라집니다.

## 라이센스

이 프로젝트는 MIT 라이센스를 따릅니다.
