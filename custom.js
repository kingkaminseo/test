function toggleDiv(event) {
    event.preventDefault();

    var div = document.getElementById("myDiv");
    var currentDisplay = div.style.display;

    if (currentDisplay === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function changeColor(event) {
    // 모든 <a> 태그에서 'selected' 클래스 제거
    const links = document.querySelectorAll('.simpleul a');
    links.forEach(link => link.classList.remove('selected'));

    // 클릭한 <a> 태그에 'selected' 클래스 추가
    const clickedLink = event.target;
    clickedLink.classList.add('selected');
}

window.addEventListener('scroll', function () {
    var banner = document.querySelector('.flip');
    var bannerHeight = banner.offsetHeight;
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    var scrollThreshold = 550; // 고정되는 스크롤 거리를 조정하세요


    if (scrollTop > scrollThreshold) {
        banner.classList.add('sticky');
    } else {
        banner.classList.remove('sticky');
    }
});




   // 메뉴 요소를 선택합니다.
   const menu = document.querySelector('.menu');

   // 메뉴 내의 링크 요소를 선택합니다.
   const links = menu.querySelectorAll('.mainnav');

   // 링크 요소에 클릭 이벤트 리스너를 추가합니다.
   links.forEach(link => {
       link.addEventListener('click', (event) => {
           event.preventDefault(); // 링크의 기본 동작을 막습니다.

           // 현재 클릭된 링크에 active 클래스를 추가하고, 이전에 active 클래스를 가진 링크에서는 제거합니다.
           links.forEach(link => {
               if (link === event.target) {
                   link.classList.add('active');
               } else {
                   link.classList.remove('active');
               }
           });
       });
   });













   var flip = document.querySelector('.flip');
   var card = document.querySelector('.card');
   var adbtn = document.querySelector('.adbtn');

   adbtn.addEventListener('click', function(event) {
       event.preventDefault(); // 기본 동작(링크 이동) 막기
       card.style.transition = 'none'; // 애니메이션 멈춤
       setTimeout(function() {
           card.style.transform = 'rotateY(180deg)'; // 회전 애니메이션 적용
           card.style.transition = ''; // 애니메이션 재개
       }, 0);
   });




   