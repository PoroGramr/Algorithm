function solution(array) {

    array.sort(function(a, b) {
  return a - b;
    });
    var arrayCenterValue = Math.floor(array.length / 2);
    
    var answer = array[arrayCenterValue]
    
    return answer;
}