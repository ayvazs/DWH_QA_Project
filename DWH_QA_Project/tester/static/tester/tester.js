function clean_status(node_id){
	document.getElementById(node_id).classList.remove('fail');
	document.getElementById(node_id).classList.remove('warn');
	document.getElementById(node_id).classList.remove('success');
}

$(document).ready(function() {
	$(".do_test_exist_btn").click(function(){
		$.ajax({
			type: "GET",
			url: "/tester/table/" + $(this).attr("data-tabid") + "/do_test_exists_on_prod/",
			success: function(data) {
				clean_status('div_exist_' + data['table_id']);
				document.getElementById('div_exist_' + data['table_id']).classList.add(data['test_status']);
				document.getElementById('div_exist_' + data['table_id']).innerHTML = data['test_message'];
			}
		})
	});

	$(".do_test_dtpc").click(function(){
		$.ajax({
			type: "GET",
			url: "/tester/table/" + $(this).attr("data-tabid") + "/do_test_dtpc/",
			success: function(data) {
				clean_status('div_dtpc_' + data['table_id']);
				document.getElementById('div_dtpc_' + data['table_id']).classList.add(data['test_status']);
				document.getElementById('div_dtpc_' + data['table_id']).innerHTML = data['test_message'];
			}
		})
	});

	$(".do_test_uniq_dev").click(function(){
		$.ajax({
			type: "GET",
			url: "/tester/table/" + $(this).attr("data-tabid") + "/do_test_uniq_dev/",
			success: function(data) {
				clean_status('div_uniq_dev_' + data['table_id']);
				document.getElementById('div_uniq_dev_' + data['table_id']).classList.add(data['test_status']);
				document.getElementById('div_uniq_dev_' + data['table_id']).innerHTML = data['test_message'];
			}
		})
	});

	$(".do_test_uniq_prod").click(function(){
		$.ajax({
			type: "GET",
			url: "/tester/table/" + $(this).attr("data-tabid") + "/do_test_uniq_prod/",
			success: function(data) {
				clean_status('div_uniq_prod_' + data['table_id']);
				document.getElementById('div_uniq_prod_' + data['table_id']).innerHTML = data['test_message'];
				document.getElementById('div_uniq_prod_' + data['table_id']).classList.add(data['test_status']);
			}
		})
	});

	$(".do_test_complete_dev").click(function(){
		$.ajax({
			type: "GET",
			url: "/tester/table/" + $(this).attr("data-tabid") + "/do_test_complete_dev/",
			success: function(data) {
				clean_status('div_complete_dev_' + data['table_id']);
				document.getElementById('div_complete_dev_' + data['table_id']).classList.add(data['test_status']);
				document.getElementById('div_complete_dev_' + data['table_id']).innerHTML = data['test_message'];
			}
		})
	});

	$(".do_test_complete_prod").click(function(){
		$.ajax({
			type: "GET",
			url: "/tester/table/" + $(this).attr("data-tabid") + "/do_test_complete_prod/",
			success: function(data) {
				clean_status('div_complete_prod_' + data['table_id']);
				document.getElementById('div_complete_prod_' + data['table_id']).classList.add(data['test_status']);
				document.getElementById('div_complete_prod_' + data['table_id']).innerHTML = data['test_message'];
			}
		})
	});

	$(".do_all_tests").click(function(){
		var divs_list = document.getElementsByClassName("status_div exist_div");
		for (i = 0; i < divs_list.length; i++) {
		    clean_status(divs_list[i].id);
		    var id = divs_list[i].id;
		    divs_list[i].innerHTML = '<img alt="loading..." src="' + loading + '" class="loading_img"/>';

			$.ajax({
				type: "GET",
				url: "/tester/table/" + $(divs_list[i]).attr('data-tabid') + "/do_test_exists_on_prod/",
				success: function(data) {
					document.getElementById('div_exist_' + data['table_id']).classList.add(data['test_status']);
					document.getElementById('div_exist_' + data['table_id']).innerHTML = data['test_message'];
				}
			})
		}

		divs_list = document.getElementsByClassName("status_div dtpc_div");
		for (i = 0; i < divs_list.length; i++) {
			clean_status(divs_list[i].id);
		    divs_list[i].innerHTML = '<img alt="loading..." src="' + loading + '" class="loading_img"/>';

			$.ajax({
				type: "GET",
				url: "/tester/table/" + $(divs_list[i]).attr('data-tabid') + "/do_test_dtpc/",
				success: function(data) {
					document.getElementById('div_dtpc_' + data['table_id']).innerHTML = data['test_message'];
					document.getElementById('div_dtpc_' + data['table_id']).classList.add(data['test_status']);
				}
			})
		}

		divs_list = document.getElementsByClassName("status_div uniq_dev_div");
		for (i = 0; i < divs_list.length; i++) {
		    clean_status(divs_list[i].id);
		    divs_list[i].innerHTML = '<img alt="loading..." src="' + loading + '" class="loading_img"/>';

			$.ajax({
				type: "GET",
				url: "/tester/table/" + $(divs_list[i]).attr('data-tabid') + "/do_test_uniq_dev/",
				success: function(data) {
					document.getElementById('div_uniq_dev_' + data['table_id']).innerHTML = data['test_message'];
					document.getElementById('div_uniq_dev_' + data['table_id']).classList.add(data['test_status']);
				}
			})
		}

		divs_list = document.getElementsByClassName("status_div uniq_prod_div");
		for (i = 0; i < divs_list.length; i++) {
			clean_status(divs_list[i].id);
		    divs_list[i].innerHTML = '<img alt="loading..." src="' + loading + '" class="loading_img"/>';

			$.ajax({
				type: "GET",
				url: "/tester/table/" + $(divs_list[i]).attr('data-tabid') + "/do_test_uniq_prod/",
				success: function(data) {
					document.getElementById('div_uniq_prod_' + data['table_id']).innerHTML = data['test_message'];
					document.getElementById('div_uniq_prod_' + data['table_id']).classList.add(data['test_status']);
				}
			})
		}

		divs_list = document.getElementsByClassName("status_div complete_dev_div");
		for (i = 0; i < divs_list.length; i++) {
			clean_status(divs_list[i].id);
		    divs_list[i].innerHTML = '<img alt="loading..." src="' + loading + '" class="loading_img"/>';

			$.ajax({
				type: "GET",
				url: "/tester/table/" + $(divs_list[i]).attr('data-tabid') + "/do_test_complete_dev/",
				success: function(data) {
					document.getElementById('div_complete_dev_' + data['table_id']).innerHTML = data['test_message'];
					document.getElementById('div_complete_dev_' + data['table_id']).classList.add(data['test_status']);
				}
			})
		}

		divs_list = document.getElementsByClassName("status_div complete_prod_div");
		for (i = 0; i < divs_list.length; i++) {
			clean_status(divs_list[i].id);
		    divs_list[i].innerHTML = '<img alt="loading..." src="' + loading + '" class="loading_img"/>';

			$.ajax({
				type: "GET",
				url: "/tester/table/" + $(divs_list[i]).attr('data-tabid') + "/do_test_complete_prod/",
				success: function(data) {
					document.getElementById('div_complete_prod_' + data['table_id']).innerHTML = data['test_message'];
					document.getElementById('div_complete_prod_' + data['table_id']).classList.add(data['test_status']);
				}
			})
		}
	});
});
