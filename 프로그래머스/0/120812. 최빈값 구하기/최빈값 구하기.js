function solution(array) {
    /*
    딕셔너리를 이용하여 각 요소별 출현 횟수를 저장한다.
    
    그 후 딕셔너리 key의 개수만큼 for문을 통해 가장 큰 값을 검사한다.
    만약 등장횟수가 동일한 수는 어떻게 검사해야 하는가?
    
    딕셔너리의 밸류만 뽑아서 정렬한 뒤 가장 마지막 값과 동일한 요소가 있다면 -1을 리턴?
    */
    
    // 숫자들의 등장 횟수를 카운트 하기 위한 map 선언
    var numberCount = new Map();
    
    // 숫자들의 등장 횟수를 카운트
    for (var i = 0; i < array.length; i++){
        
        // 만약 배열의 그 숫자를 처음 카운트한다면
        if(numberCount.get(array[i]) == null)
            numberCount.set(array[i], 1);
        
        // 이미 이전에 등장했던 숫자라면 + 1
        else{
            numberCount.set(array[i], numberCount.get(array[i]) + 1);
        }
    }
    
    // 최빈값을 찾는 for문
    var answer = 0;
    var checkNum = 0;
    numberCount.forEach(function(key,value){
        
        // for문을 돌며 최빈값을 검색한다.
        if(checkNum < key){
            checkNum = key;
            answer = value;
        }
    })
    
    
    // 최빈값이 2개 이상인지 확인하는 for문
    var sameCount = 0
    numberCount.forEach(function(key,value){
        if(checkNum == key){
            sameCount++;
        }
    })
    
    if(sameCount <= 1){
        return answer;
    }
    else{
        return -1;
    }
}
