// content of plugins/axios.js
/* 
// This is a global config declaration that works on any axios instance,
// meaning that if you just import axios from 'axios' in any place, you will get those.
// This will also work on the axios instance that nuxt creates and injects.

import axios from 'axios'

axios.defaults.xsrfHeaderName = 'x-csrftoken'
axios.defaults.xsrfCookieName = 'csrftoken'
*/
export default function ({ $axios }) {
    // This is a nuxt specific instance config, this will work in
    // everyplace where nuxt inject axios, like Vue components, and store
    $axios.defaults.xsrfHeaderName = 'x-csrftoken'
    $axios.defaults.xsrfCookieName = 'csrftoken'
    $axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    $axios.defaults.headers['Content-Type'] = 'application/json'
}