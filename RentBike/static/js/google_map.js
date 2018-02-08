var map, infoWindow;

var markersData = [
	{
		lat: 53.893001,
		lng: 27.603587,
		name: "Название 1",
		address:"Адрес 1"
	},
	{
		lat: 53.930904,
		lng: 27.519106,
		name: "Название 2",
		address:"Адрес 2"
	},
	{
		lat: 53.870899,
		lng: 27.517329,
		name: "Название 3",
		address:"Адрес 3"
	}
];

function initMap() {
    var myCenter = new google.maps.LatLng(53.9023238, 27.5618025);
    var mapProp = {center:myCenter, zoom:12, scrollwheel:true, draggable:true, mapTypeId:google.maps.MapTypeId.ROADMAP};
    map = new google.maps.Map(document.getElementById("googleMap"), mapProp);

    // Создаем объект информационного окна и помещаем его в переменную infoWindow
    infoWindow = new google.maps.InfoWindow();
    // Отслеживаем клик в любом месте карты
    google.maps.event.addListener(map, "click", function() {
        infoWindow.close();
    });
    // Определяем границы видимой области карты в соответствии с положением маркеров
    var bounds = new google.maps.LatLngBounds();
    // Перебираем в цикле все координаты, хранящиеся в markersData
    for (var i = 0; i < markersData.length; i++){
        var latLng = new google.maps.LatLng(markersData[i].lat, markersData[i].lng);
        var name = markersData[i].name;
        var address = markersData[i].address;
        // Добавляем маркер с информационным окном
        addMarker(latLng, name, address);
        // Расширяем границы нашей видимой области, добавив координаты нашего текущего маркера
        bounds.extend(latLng);
    }
    // Автоматически масштабируем карту так, чтобы все маркеры были в видимой области карты
    map.fitBounds(bounds);
}

// Функция добавления маркера с информационным окном
function addMarker(latLng, name, address) {
    var marker = new google.maps.Marker({
        position: latLng,
        map: map,
        title: name
    });
    // Отслеживаем клик по нашему маркеру
    google.maps.event.addListener(marker, "click", function() {
        // contentString — это переменная в которой хранится содержимое информационного окна.
        var contentString = '<div class="infowindow">' +
                                '<h4>' + name + '</h4>' +
                                '<p>' + address + '</p>' +
                            '</div>';
        // Меняем содержимое информационного окна
        infoWindow.setContent(contentString);
        // Показываем информационное окно
        infoWindow.open(map, marker);
    });
}

