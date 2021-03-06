window.addEventListener("load", function(){
    /* Install Websocket listener
    Data from Django:
    - DJANGO_URL  : Use to link Websockets to the server.
    - app_settings: Aplication settings like:
                    - members_maxi  : Maxi of team members list.
                    - columns_number: Number of columns in the web rendering page.
                    - log: True/False to trace with console.log()
    - page_boot_db: Members list on first diplay page from Django.
    */
    const log = app_settings.log;
    let wamp_url
    // Get hostname from DJANGO_URL
    const hostname = DJANGO_URL;
    // Wamp url https adaptation
    if (hostname === "127.0.0.1") {
        wamp_url = 'ws://' + hostname + ':8080/ws';
    } else {
        wamp_url = "wss://" + hostname + "/ws";
    }

    /* ==== Display members colums on boot page ==== */
    if (log===true) { console.log("main.js: starting create 'list_member_container'...")}
    update_total_count(page_boot_db, app_settings.members_maxi);
    draw_colums(app_settings, "list_member_container", page_boot_db, log);

    /* ==== Connection configuration to our WAMP router ==== */
    let connection = new autobahn.Connection({
        url: wamp_url,  // default url= url: 'ws://127.0.0.1:8080/ws'
        realm: 'realm1'
    });
    if (log === true) { console.log("main.js: Autobahn definition with: " + wamp_url) }

    /* ==== Connection opened ==== */
    connection.onopen = function(session) {
        console.log("main.js: Websocket connected!");
        // ==== RUNTIME CHANNEL ====
        //When we receive the 'argonautes_channel' event, REMOVE/DRAW the page columns.
        session.subscribe('argonautes_channel', function(args){
            // get team_list_json from python autobahn websocket
            let members_data = args[0];
            if (members_data !== "") {
                update_total_count(members_data, app_settings.members_maxi);
                draw_colums(app_settings, "list_member_container", members_data, log);
                console.log("main.js: Page updated!");
            }
        }); //subscribe
    } //onopen
    // Open the WAMP connection with the router.
    connection.open();
}); //addEventListener
