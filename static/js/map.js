var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new kakao.maps.LatLng(37.56646, 126.98121), // 지도의 중심좌표
        level: 4, // 지도의 확대 레벨
        mapTypeId: kakao.maps.MapTypeId.ROADMAP // 지도종류
    };

// 지도를 생성한다
var map = new kakao.maps.Map(mapContainer, mapOption);
var final
function locationLoadSuccess(pos) {
    // 현재 위치 받아오기
    var currentPos = new kakao.maps.LatLng(pos.coords.latitude, pos.coords.longitude);

    // 지도 이동(기존 위치와 가깝다면 부드럽게 이동)
    map.panTo(currentPos);

    // 마커 생성
    var marker = new kakao.maps.Marker({
        position: currentPos
    });

    // 기존에 마커가 있다면 제거
    marker.setMap(null);
    marker.setMap(map);
}

function locationLoadError(pos) {
    alert('위치 정보를 가져오는데 실패했습니다.');
}

// 위치 가져오기 버튼 클릭시
function getCurrentPosBtn() {
    navigator.geolocation.getCurrentPosition(locationLoadSuccess, locationLoadError);
    setTimeout(locationSearch, 3000)


    // kakao.maps.load(function () {
    // });
    // var bounds = map.getBounds();
    // var swLatLng = bounds.getSouthWest();
    // var neLatLng = bounds.getNorthEast();
    // console.log(swLatLng, neLatLng);

}

function getAddr(lat,lng){


    $.ajax({
        url: 'https://dapi.kakao.com/v2/local/geo/coord2address.json?',
        type: 'GET',
        data: {x:lng,y:lat},
        headers: {'Authorization': 'KakaoAK 0f23477b2b3262f820c688ff81fdf916'},
        success: function (data) {
            let result = data.documents
            final= result[0].address.region_3depth_name;

        },
        error: function (e) {
            console.log(e);
        }
    });

}

function locationSearch() {


    var infowindow = new kakao.maps.InfoWindow({zIndex: 1});


    var position = map.getCenter().toString();

    var result = position.split(/[(, )]/)
    let lat = result[1];
    let lng = result[3];
    console.log(final);

    getAddr(lat, lng);


    $.ajax({
        url: 'https://dapi.kakao.com/v2/local/search/category.json?',
        type: 'GET',
        data: {category_group_code:'FD6',x:lng,y:lat},
        headers: {'Authorization': 'KakaoAK 0f23477b2b3262f820c688ff81fdf916'},
        success: function (data) {
            console.log(data.documents[0]);
            document.getElementById('#search-result').innerText = data.documents[0].address_name;
            // for (var i=0; i < data.documents.length; i++) {
            //     document.getElementById('#search-result').innerHTML = data.documents[i];
            // }


            placesSearchCB()
        },
        error: function (e) {
            console.log(e);
        }
    });

// 카테고리로 은행을 검색합니다
//     ps.categorySearch('FD6', placesSearchCB, {useMapBounds: true});
//
// 키워드 검색 완료 시 호출되는 콜백함수 입니다
    function placesSearchCB(data, status, pagination) {
        if (status === kakao.maps.services.Status.OK) {
            for (var i = 0; i < data.length; i++) {
                displayMarker(data[i]);
            }
        }
    }

// 지도에 마커를 표시하는 함수입니다
    function displayMarker(place) {
        // 마커를 생성하고 지도에 표시합니다
        var marker = new kakao.maps.Marker({
            map: map,
            position: new kakao.maps.LatLng(place.y, place.x)
        });

        // 마커에 클릭이벤트를 등록합니다
        kakao.maps.event.addListener(marker, 'click', function () {
            // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
            infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
            infowindow.open(map, marker);
        });
    }

}