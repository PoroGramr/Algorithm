function solution(numer1, denom1, numer2, denom2) {
    /*
    분수1을 통분한 결과값을 저장하는 sameNumer1 sameDenom1을 선언하고 분수2와 통분해준다.
    분수2을 통분한 결과값을 저장하는 sameNumer2 sameDenom2을 선언하고 분수1와 통분해준다. 
    
    그 후 분자를 더해 addNumer라는 변수를 선언해 저장한다
    
    마지막으로 결과값 분모와 분자의 최대 공약수를 구해 존재한다면 약분해주고,
    존재하지 않는다면 그대로 리턴한다.
    */
    
    // 결과값 출력을 위한 변수 선언
    var answer = [];
    
    // 분수1을 분수2와 통분한 결과값을 저장
    // 각각 분수1의 분모와 분자에 분수2의 분모를 곱한다.(통분)
    var sameNumer1 = numer1 * denom2;
    var sameDenom1 = denom1 * denom2;
    
    // 분수2를 분수1과 통분한 결과값을 저장
    // 각각 분수2의 분모와 분자에 분수1의 분모를 곱한다.(통분)
    var sameNumer2 = numer2 * denom1;
    var sameDenom2 = denom2 * denom1;
    
    // 통분한 두 분수를 더한 값을 저장
    var addNumer = sameNumer1 + sameNumer2;
    var addDenom = sameDenom1;
    
    // 통분한 분수의 분자는 addNumer, 분모는 addDenom
    
    //분자와 분모의 최대 공약수를 계산하는 함수 선언
    var getGcd = (a, b) => (a % b == 0 ? b : getGcd(b, a % b));
    
    // 최대 공약수를 계산
    var gcd = getGcd(addNumer, addDenom);
    
    // 계산한 최대공약수를 바탕으로 결과값 배열에 선언
    answer = [addNumer / gcd, addDenom / gcd];
    
    return answer;
}