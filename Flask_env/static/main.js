const { createApp } = Vue

const TaskApp = {
    data(){
        return {
            task: 'New Task',
            tasks: [
                {title: 'One'},
                {title: 'Two'}
            ]
        }
    },
    delimiters: ['{','}']
}


createApp(TaskApp).mount('#app')