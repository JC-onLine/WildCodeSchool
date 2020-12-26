
/* ==== FUNCTION TOOLS ==== */

function draw_column(root_div, column_data, log) {
    //              Create a column in DOM 
    // :param:  'root_div':     Create colums from 'root_div'.
    // :param:  'column_data'   Data to display.
    // :param:  'log':          Trace on browser console.

    if (log===true) { console.log("tools.js: START "); }
    let column_div;
    let member_div;
    let member_id;
    // create column div
    column_div = document.createElement("div");
    column_div.setAttribute("class", "member-list");
    column_data.forEach(function(member_name, index) {
        if (log===true) { console.log("tools.js: forEach: " + member_name); }
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

function draw_3_colums(root_id, data, log) {
    //      Create multiple columns in DOM
    // :param:  'root_id':  Create colums from <div id=root_id>.
    // :param:  'data'      Data to display.
    // :param:  'log':      Trace on browser console.
    if (log===true) { console.log("draw_3_colums.js: starting create 'div_container'...")};
    let div_root = document.getElementById(root_id);
    let div_container_root = document.createElement("div");
    div_container_root.id = 'div_container';
    div_container_root.setAttribute("class", "div_container");
    if (log===true) { console.log(
        "draw_3_colums.js: 'team_list_on_first_open.topic' " + team_list_on_first_open.topic
    )};
    // draw column 1,2 and in DOM
    draw_column(div_container_root, data.topic.column1, log);
    draw_column(div_container_root, data.topic.column2, log);
    draw_column(div_container_root, data.topic.column3, log);
    div_root.appendChild(div_container_root);
    console.log("draw_3_colums.js: DOM create done.");
}