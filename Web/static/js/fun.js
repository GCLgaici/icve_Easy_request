// 设置cookie，days有效期天数
function setCookie(name,value,days){
    let date = new Date()
    date.setTime(date.getTime() + days*24*60*60*1000)
    document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`
}

// 获取cookie
function getCookie(name){
    let arr = document.cookie.split('; ')
    for(let item of arr){
        let kv = item.split('=')
        if(kv[0] === name) return kv[1]
    }
    return ""
}

// 使用示例
// setCookie("token","abc123token",7) // 保存7天
// let token = getCookie("token")


