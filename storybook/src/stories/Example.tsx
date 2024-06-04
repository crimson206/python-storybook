/**
 *
 * {'docs': None,
 'name': 'reculsive_rag',
 'render_name': 'reculsive_rag',
 'result': '{"file1": "Hello world.", "file2": "This is a book."}',
 'title': 'Example/String',
 'type_hints': {'query': 'str', 'return': 'str'}}
 * 
 */

interface py_reculsive_rag_props {
    query: py_str
}

 const py_reculsive_rag = ({query}:py_reculsive_rag_props): py_Dict => {
    return {'str':"hi"}
 }