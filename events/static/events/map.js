ymaps.ready(init);
function init () {
    var myMap = new ymaps.Map('map', {
            center: [55.7887, 49.1221],
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search'
        }),
        objectManager = new ymaps.ObjectManager({
            // Чтобы метки начали кластеризоваться, выставляем опцию.
            clusterize: true,
            // ObjectManager принимает те же опции, что и кластеризатор.
            gridSize: 32,
            clusterDisableClickZoom: true
        });
    myMap.geoObjects.add(objectManager);
    $.ajax({
        url: "http://localhost:8000/static/events/data.json"
    }).done(function(data) {
        objectManager.add(data);
    });
}
