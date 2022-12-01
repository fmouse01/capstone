

const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return{
        message: 'Is this working?',
        userCalories: 0,
        dailyCalories: 1650,
        totalCalories: 0,
   
        

        }
    },
    methods:{
        // getNewQuestion(){
        //     // this.hideContent()
        //     axios({
        //         method: 'get',
        //         url:  `https://opentdb.com/api.php`,
        //         params: {
        //             amount: this.userAmount,
        //             type: this.userType,
        //             difficulty: this.userDifficulty,
        //             category: this.userCategory,
                    
        //         }
        //     }).then((response)=> {
        //         this.questionArray = response.data.results
                
        //         this.checkAnswers()
                
        //         // console.log(this.currentQuestion.incorrect_answers[0])
        //         // this.revealContent()
        //         this.inGame = true
        //     }),

        calorieCalculator(){
            
            this.totalCalories = this.dailyCalories - this.userCalories
            this.dailyCalories = this.totalCalories
            
        },
        
        
        
    },
    mounted(){
        console.log('hello')
        console.log(this.calorieCalculator())
       
      
       
    }
})