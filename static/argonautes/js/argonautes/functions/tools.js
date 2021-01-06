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
        if (log === true) { console.log("tools.js/draw_column: " +column_id +" "+member_name); }
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

function update_total_count(members_data, maxi){
    let members_total_count = calcul_total(members_data)
    document.getElementById("total-count").textContent = members_total_count;
    if (members_total_count >= maxi) {
        document.getElementById("send-button").
            setAttribute("disabled", "disabled");
        document.getElementById("name").
            setAttribute("disabled", "disabled");
        document.getElementById("name").placeholder = " C'est complet !";
        document.getElementById("name").className = "full";
    }
}

function draw_colums(app_settings, target_container, members_data_json, log) {
    if (log===true) { console.log("draw_colums.js: "+members_data_json+".column1=" + members_data_json.column1)}
    if (members_data_json !== "") {
        if (log===true) { console.log("draw_colums.js: boot_page_db = null")}
        // ==== /!\ page_boot_db = null; /!\
        let node_container = document.getElementById(target_container);
        // remove node_container
        if (node_container) {
            if (log === true) {
                console.log("draw_colums.js: start remove " + target_container + "...")
            }
            node_container.remove();
            if (log === true) {
                console.log("draw_colums.js: '" + target_container + "' removed.")
            }
        }
        if (log === true) { console.log("draw_colums.js: '"+ target_container +"' not found: Create it!");}
        if (log === true) { console.log("draw_colums.js: starting create '" +target_container +"'...")}
        let section = document.getElementById("team-list-section");
        let target_container_new = document.createElement("div");
        target_container_new.id = target_container;
        target_container_new.setAttribute("class", target_container);
        if (log===true) { console.log("draw_colums.js: 'target_container_new' " + target_container_new)}
        // draw column 1,2 and in DOM
        console.log("typeof: " + typeof (members_data_json));
        for (let column in members_data_json) {
            console.log("draw_colums: column=" + column);
            draw_column(column, target_container_new, members_data_json[column], log);
            // column++;
        }
        // draw_column(1, target_container_new, members_data_json.column1, log);
        // draw_column(2, target_container_new, members_data_json.column2, log);
        // draw_column(3, target_container_new, members_data_json.column3, log);
        section.appendChild(target_container_new);
        if (log === true) { console.log("draw_colums.js: DOM create done."); }
    }
}

function calcul_total(data) {
    return  data.column1.length +
            data.column2.length +
            data.column3.length;
}
