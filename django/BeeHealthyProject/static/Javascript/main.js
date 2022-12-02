

const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return{
        message: 'Is this working?',
        userCalories: 0,
        dailyCalories: 1650,
        totalCalories: 0,
        calorieArray: [],
        foodItem: '',
   
        

        }
    },
    methods:{
        // getCalories(){
        //     axios({
        //         method: 'get',
        //         url:  `https://api.myfitnesspal.com/v2/diary`,
        //         params: {
        //             get: this.userAmount,
        //             post: this.userType,
        //             delete: this.userDifficulty,
        //             patch: this.userCategory,
                    
        //         },
        //     }).then((response)=> {
        //         this.calorieArray = response.data.results
                
        //         this.checkAnswers()
                
        //         console.log(calorieArray)
        //         console.log(foodItem)
        //     })
        // },
        calorieCalculator(){
            
            this.totalCalories = this.dailyCalories - this.userCalories
            this.dailyCalories = this.totalCalories
            
        },
        
        
        
    },
    mounted(){
        console.log('hello')
    
       
      
       
    },
})