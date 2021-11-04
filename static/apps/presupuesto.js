var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
        return {
            trabajos: [],
            counter:0,
            cant : [],
            sub : 0,
        };
    },
    methods: {        
        getTrabajos() {
            fetch(`/api/trabajos`)
                .then(response => response.json())
                .then(result => {
                    console.log(result)
                    this.trabajos = result.data
                })
        },
    },
    created() {
        this.getTrabajos()
        console.log('Pagina Cargada')
    },   
});

document.addEventListener('DOMContentLoaded', function () {
    var Modalelem = document.querySelector('.modal');
    var instance = M.Modal.init(Modalelem);
    instance.open();
});