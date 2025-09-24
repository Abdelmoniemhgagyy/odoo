/** @odoo-module **/
import { Component , useState , onWillUnmount } from "@odoo/owl";

import { rpc } from "@web/core/network/rpc";
import { registry } from "@web/core/registry";

class TodoList extends Component{

    static template = "todo_list.TodoListView";
    setup(){
    this.state = useState({
    'records':[],
    'currentRecord':{},
    'is_edit':false,
    'name':"",
    'is_done':false,
    'is_complete':false
        })
    this.viewlist();
    this.timer = setInterval(() => this.viewlist(), 3000);
    this.deleteTask = this.deleteTask.bind(this);
    }
    onWillUnmount(){
        clearInterval(this.timer)
    }
//  Change value of is done
   async toggleTask(record) {
    await rpc('/web/dataset/call_kw', {
        model: 'todo.list',
        method: 'write',
        args: [[record.id], {is_done: !record.is_done}],
        kwargs: {},
    });
    this.viewlist();
}
// Show Tasks
   async viewlist(){
   if (this.state.is_complete) {
       const data = await rpc('/web/dataset/call_kw', {
            model: 'todo.list', method: 'search_read',
            args: [[['is_done','=',true]]],
            kwargs: {},
        })
            this.state.records = data
        }
   else {
       const data = await rpc('/web/dataset/call_kw', {
            model: 'todo.list', method: 'search_read',
            args: [],
            kwargs: {},
        })
           this.state.records = data
}
    }

   async createTask(){
    await rpc('/web/dataset/call_kw', {
            model: 'todo.list', method: 'create',
            args: [{
            'name':this.state.name,
            'is_done':this.state.is_done}],
            kwargs: {},
        });
        this.state.name = ''
        this.viewlist();
    }

   async deleteTask(recordId){
        await rpc('/web/dataset/call_kw', {
            model: 'todo.list', method: 'unlink',
            args: [recordId],
            kwargs: {},
         });
          this.viewlist();
        }

   editTask(rec) {
    this.state.currentRecord = rec;
    this.state.name = rec.name;
    this.state.is_done = rec.is_done;
    this.state.is_edit = true
}

   resetTask(){
    this.state.currentRecord = {};
    this.state.name = "";
    this.state.is_done = false;
    this.state.is_edit = false
 }

   async updateTask() {
    const record = this.state.currentRecord
        await rpc("/web/dataset/call_kw", {
            model: "todo.list",
            method: "write",
            args: [[record.id],{'name':this.state.name,'is_done':this.state.is_done}],
            kwargs: {},
        });
            this.viewlist();
            this.resetTask()
        }

    }

registry.category("actions").add('todo_list.todo_list_view',TodoList);
