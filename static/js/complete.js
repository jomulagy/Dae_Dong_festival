function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function pay_yes(){
    //데이터 넣기
    var order_final = new Array();
    var data = new Object();
    data.table_num = localStorage.getItem('table_number');
    data.phone_num = localStorage.getItem('phone_number');
    data.menus = localStorage.getItem('order');
    order_final.push(data)

    //정보 전송
    const request = new XMLHttpRequest();
    request.open('POST', '/order/create', true);
    //타입 JSON
    request.setRequestHeader('Content-type', 'application/json');
    const csrftoken = getCookie('csrftoken'); // csrftoken 가져오기
    request.setRequestHeader('X-CSRFToken', csrftoken);
    request.send(JSON.stringify(order_final))


    request.onreadystatechange = function(event){
        // 1) 데이터를 다 받았고, 2) 응답코드 200(성공)을 받았는지 체크
        if(request.readyState == 4 && request.status == 200){
            //local storage 초기화
            localStorage.clear();
            location.replace('/complete')
        }else{
            alert("주문 정보 전송 실패")
        }
    }

    
    





}

function pay_no(){
    localStorage.clear();
    location.replace('/');
}
