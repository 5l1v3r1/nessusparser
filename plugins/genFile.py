from plugins import selects

def genr(cb, plugin_ids, name, description, risk_description, recommendation, notes):
	pluginid_strings = [x for x in plugin_ids if not isinstance(x, int)]
	pluginid_ints = [x for x in plugin_ids if isinstance(x, int)]

	all_rows = []

	if not len(pluginid_strings) == 0:
		all_rows += selects.pluginName(pluginid_strings, cb)
	if not len(pluginid_ints) == 0:
		all_rows += selects.pluginId(pluginid_ints, cb)
	
	all_rows = [*{*all_rows}]
	
	if len(all_rows) > 0:
		with open('./' + cb + '.txt', "a") as t_file:
			t_file.write(name + '\n' + description + '\n' + risk_description + '\n' + recommendation + '\n' + notes + '\nAffected hosts:\n')
			[ t_file.write(str(append_line[0] + '\n')) for append_line in all_rows ]
			t_file.write('\n\n\n') 
