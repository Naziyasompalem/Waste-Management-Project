const app = new Vue({
    el: "#app",
    data: {
        message: "カードを動かさないで下さい カードを読み取り中. . .",
        seen: false
    },
    methods: {
        move() {
            const se = new Audio("sound/SUICA.mp3")
            se.play()

            this.seen = true

            this.seen = true

            setTimeout(() => {
                this.message = "カードを動かさないで下さい 読み取れました. . ."
            }, 700)

            setTimeout(() => {
                this.message = "カードを動かさないで下さい サーバーと接続中. . ."
            }, 1000)

            setTimeout(() => {
                this.message = "カードを動かさないで下さい 完了. . ."
            }, 2400)

            setTimeout(() => {
                this.message = "カードを動かさないで下さい 決済中. . ."
            }, 2700)

            setTimeout(() => {
                this.message = "カードを動かさないで下さい 完了. . ."
            }, 3200)

            setTimeout(() => {
                location.href = "{% url 'successPage' %}"
            }, 3600)
        }

    }
})