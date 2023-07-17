function solution(s) {
    var answer = '';
    let arr=[];

    for(let i=0; i<=arr.length; i++){
        if(i%2 === 0){
            answer+=s.charAt(i).toUpperCase()
        }else{
            answer+=s.charAt(i)
        }
    }
    return answer;
}
