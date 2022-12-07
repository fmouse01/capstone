

const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return{
        message: 'Is this working?',
        userCalories: 0,
        dailyCalories: 0,
        totalCalories: 0,
        BMR: 0,

        userWeight: 244,
        userHeight: 70,
        userAge: 33,
        
        // gender: True
   
        

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
        getBMR(){
            // if (gender == True)
                
                const BMR = 66.47 + (6.24 * this.userWeight) + (12.7 * this.userHeight) - (6.75 * this.userAge)
            
                this.dailyCalories = Math.round(BMR) 
                
                console.log(BMR)
                console.log(this.dailyCalories)
                // BMR = 65.51 + (4.35 * this.userWeight) + (4.7 * this.userHeight) - (4.7 * this.userAge)
        },
        
        
        
        
    },
    mounted(){
        console.log('hello')
        this.getBMR()
       
      
       
    },
})