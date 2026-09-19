// Copyright (c) 2026, 	 and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Practice Task", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Practice Task", {
    refresh(frm) {
        frappe.msgprint("Practice Task JS is loading!");
    },
    refresh(frm) {
    frm.set_df_property(
        "task_title",
        "read_only",
        frm.doc.completed ? 1 : 0
    );
    },

    completed(frm) {
        frm.set_df_property(
            "task_title",
            "read_only",
            frm.doc.completed ? 1 : 0
        );
}
});
