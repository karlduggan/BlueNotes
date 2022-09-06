<template>
    <p>{{this.daysRemaining()}}</p>
</template>

<script>
export default {
    name: "CountDownComponent",
    components: {},
    props: {complete_date: String},
    mounted(){
        this.date = this.complete_date
    },  

    data(){
        return {
            date: null
        }
    },
    methods: {
        getDate: function(){
            console.log(this.complete_date)
           this.daysRemaining()
         
        },
        getDateAsArray: function(){
            let stringDate = this.complete_date;
            let stringArray = stringDate.split('-')
            const arrrOfNum = stringArray.map(str => {
                return Number(str)
            })
            let result = arrrOfNum
            return result
        },
        daysRemaining: function(){
            var dueDate, today, dDate, diff, numberOfDays, year;
            dueDate = this.getDateAsArray(); // Will need to get the month and day from props "complete_date"
            
            today = new Date();
            dDate = new Date(today.getFullYear(), dueDate[1]-1, dueDate[0]);
            year = today.getFullYear();
    
            if(today.getTime() > dDate.getTime()){
                dDate.setFullYear(dDate.getFullYear()+1);
            }
            diff = dDate.getTime() - today.getTime();
            numberOfDays = Math.floor(diff/(1000*60*60*24)) + 1 ;
            if (numberOfDays >= 365 && year == dueDate[2]){
                return "Due Today";
            }
            if(numberOfDays == 1){
                return "Due Tomorrow";
            }
            else {
               return numberOfDays + " Days " 
            }

        }
    }


}
</script>

<style lang="scss" scoped >

p {
 color: $white;
}
</style>