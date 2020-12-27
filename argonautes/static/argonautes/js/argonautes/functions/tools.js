/* ==== FUNCTION TOOLS ==== */

function draw_column(column_id, root_div, column_data, log) {
    //              Create a column in DOM 
    // :param:  'root_div':     Create colums from 'root_div'.
    // :param:  'column_data'   Data to display.
    // :param:  'log':          Trace on browser console.

    if (log===true) { console.log("tools.js/draw_column: " +column_id +" START "); }
    let column_div, member_div, member_id
    let counter_div;
    // create column div
    column_div = document.createElement("div");
    column_div.setAttribute("class", "member-list");
    // create counter_div
    counter_div = document.createElement("div");
    counter_div.id = "member_count"+column_id;
    counter_div.setAttribute("class", "count member-count");
    counter_div.textContent = column_data.length;
    column_div.appendChild(counter_div);
    column_data.forEach(function(member_name, index) {
        // if (log===true) { console.log("tools.js/draw_column: " +column_id +" "+member_name); }
        // create member div
        member_div = document.createElement("div");
        member_id = index+1;
        member_div.id = 'member_div'+member_id;
        member_div.setAttribute("class", "member-item");
        member_div.textContent = member_name;
        // add to container
        column_div.appendChild(member_div);
    })
    root_div.appendChild(column_div);
}

/*
function draw_3_colums(target_container, data, log) {
    //      Create 3 columns in DOM to display team members
    // :param:  'root_id':  Create colums from <div id=root_id>.
    // :param:  'data'      Data to display.
    if (log===true) { console.log("tools.js/draw_3_colums: starting create 'div_container'...")};
    // :param:  'log':      Trace on browser console.
    // let div_root = document.getElementById(target_container);
    // let div_container_root = document.createElement("div");
    // div_container_root.id = 'div_container';
    // div_container_root.setAttribute("class", "div_container");
    if (log===true) { console.log(
        "tools.js/draw_3_colums.js: 'team_list_on_first_open.topic' " + boot_page_db.topic
    )};
    // // draw column 1,2 and in DOM
    // draw_column(1, target_container, data.topic.column1, log);
    // draw_column(2, target_container, data.topic.column2, log);
    // draw_column(3, target_container, data.topic.column3, log);
    // div_root.appendChild(target_container);
    console.log("tools.js/draw_3_colums.: DOM create done.");
}
*/

function calcul_total(data) {
    return  data.topic.column1.length +
            data.topic.column2.length +
            data.topic.column3.length;
}
