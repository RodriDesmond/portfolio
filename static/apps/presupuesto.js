var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data() {
        return {
            trabajos: [],
        }
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
    }
});