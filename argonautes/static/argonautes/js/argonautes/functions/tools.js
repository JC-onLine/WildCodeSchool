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

function draw_colums(target_container, members_data_json, log) {
    if (log===true) { console.log("draw_colums.js: team_list_json.topic=" + team_list_json.topic)}
    if (team_list_json.topic !== "") {
        if (log===true) { console.log("draw_colums.js: boot_page_db = null")}
        boot_page_db = null;
        if (log===true) { console.log("draw_colums.js: start remove list_member_container...")}
        node_container = document.getElementById("list_member_container");
        // remove node_container
        if (node_container) {
            node_container.remove();
            if (log===true) { console.log("draw_colums.js: 'list_member_container' removed.")}

            if (log===true) { console.log("draw_colums.js: starting create 'list_member_container'...")}
            let section = document.getElementById("team-list-section");
            let list_member_container_new = document.createElement("div");
            list_member_container_new.id = 'list_member_container';
            list_member_container_new.setAttribute("class", "list_member_container");
            if (log===true) { console.log("draw_colums.js: 'list_member_container_new' " + list_member_container_new)}

            // draw column 1,2 and in DOM
            let members_total_count = calcul_total(members_data_json)
            document.getElementById("total-count").textContent = members_total_count;
            // disable input form if > MEMBERS_MAXI
            if (members_total_count >= MEMBERS_MAXI) {
                document.getElementById("send-button").
                    setAttribute("disabled", "disabled");
                document.getElementById("name").
                    setAttribute("disabled", "disabled");
                document.getElementById("name").placeholder = " C'est complet !";
                document.getElementById("name").className = "full";
            }
            draw_column(1, list_member_container_new, members_data_json.topic.column1, log);
            draw_column(2, list_member_container_new, members_data_json.topic.column2, log);
            draw_column(3, list_member_container_new, members_data_json.topic.column3, log);
            section.appendChild(list_member_container_new);
            console.log("draw_colums.js: DOM create done.");
        }else{
            console.log("draw_colums.js: 'node_container' not found.");
        }
    }
}

function calcul_total(data) {
    return  data.topic.column1.length +
            data.topic.column2.length +
            data.topic.column3.length;
}
