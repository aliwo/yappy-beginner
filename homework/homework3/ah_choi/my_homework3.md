## 고오~급 git 문제 (@ah_choi)


### 다른 브렌치에서 1개의 커밋만 가져오고 싶다면 어떻게 할까요?
cherry-pick을 이용하여 다른 브랜치의 특정 커밋을 복사해서 내 브랜치로 가져온다.

### 10개의 파일을 stage에 올리고 커밋했는데, 그 중 5개의 파일이 잘못됬다는 걸 알았다면 어떻게 해결할까요? (여러가지 답이 있어요)
1. 커밋 전으로 reset한 후, 잘못된 파일을 수정하여 10개의 파일을 다시 commit한다.
2. 커밋 전으로 revert한 후, 잘못된 파일을 수정하여 10개의 파일을 다시 commit한다.
- reset은 특정 commit 이후의 내용과 이력을 모두 날린다. push한 경우 쓸 수 없다.
- revert는 특정 commit의 내용만을 날린다. 이력은 그대로 남긴다.
* reset 옵션
1) soft
index 보존, 이후 파일 내용 보존
2) mixed (기본)
index 취소, 이후 파일 내용 보존
3) hard
index 취소, 이후 파일 내용 삭제
-- index 보존 = staged 상태 보존?