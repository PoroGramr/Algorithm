function solution(num_list) {
    var answer = [];
    for(var i = num_list.length; i > 0; i--){
        answer.push(num_list[i - 1]);
    }
    
    return answer;
}