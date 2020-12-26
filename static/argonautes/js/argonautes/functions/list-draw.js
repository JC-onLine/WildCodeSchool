function draw_column(root_div, column_data, log) {
//              Create a column from
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

    // member_div.setAttribute("title", "json");
    // add container and row
    // div_container_new.appendChild(member_div);
    // set value
    // document.getElementById('member_div'+member_id).innerHTML = "AZERTY";
    // return(member_div)
}