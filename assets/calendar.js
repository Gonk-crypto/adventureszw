import React from 'react';
import ReactDOM from 'react-dom';
import CalendarApp from './calendar/container/Root';
import axios from 'axios';

const calendar = document.getElementById('calendar-root');
console.log(calendar)
if(calendar){
    ReactDOM.render(<CalendarApp
                        showMonth
                        monthHook={(month, year, component)=>{
                            axios({
                                method: 'GET',
                                url: `/api/events/${year}/${month}`
                            }).then(res =>{
                                component.setState({
                                    events: res.data.map(evt =>({
                                        id: evt.id,
                                        date: new Date(evt.date),
                                        title: evt.title
                                    }))
                                })
                            })
                        }} />, calendar);

}