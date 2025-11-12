const input_df = document.getElementById('df_csv') 
const iv_select =  document.getElementById('iv')
const dv_select =  document.getElementById('dv')
const form_container = document.getElementById('form_container')
const info_container = document.getElementById('info_container')

let iv_list = []
let dv_list = []


iv_select.style.visibility = "hidden"
dv_select.style.visibility = "hidden"

input_df.addEventListener('change', () =>{
        iv_select.innerHTML = ''
        dv_select.innerHTML = ''
        let file_reader = new FileReader()
        file_reader.readAsText(input_df.files[0])

        file_reader.addEventListener('load', () => {    //Gets column line of csv file
                const contents = file_reader.result;
                const columns = contents.split('\n')[0].split(',')

                for(let column of columns){
                    iv_select.add(new Option(column,column))
                    dv_select.add(new Option(column,column))
                }
                iv_select.style.visibility = "visible"
                dv_select.style.visibility = "visible"
                iv_select.size = "4"
                dv_select.size = "4"
            })
        console.log(input_df.files[0].name)
    })

function push_info(){
    for(let i = 0; i < iv_select.selectedOptions.length; i++ ){
        iv_list.push(iv_select.selectedOptions[i].value)
        console.log(iv_list[i])
    }
    for(let i = 0; i < dv_select.selectedOptions.length; i++ ){
        dv_list.push(dv_select.selectedOptions[i].value)
        console.log(dv_list[i])
    }
    console.log(`iv len: ${iv_list.length}`)

    //Hide main container
    form_container.style.display = "none"
    
}


function deliver(){
    info_container.style.display = "inline"
    console.log("howdy")
    console.log(`iv len: ${iv_list.length}`)
}

