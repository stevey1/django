# in order for op_name to work, need to fix graphene_django.utils.testing operation_name->operationName
queries = '''
    query getCategory {
        allCategories {
            pageInfo {
                hasNextPage
                }
            }
    }
    mutation updateCategory($name: String!) {
        updateCategory(name: $name) {
    		errors{
                field
                messages
            }
            category {
                id
                name
            }
        }
    }
    mutation updateCategoryByForm {
        updateCategoryByForm(input: {name:"test123"}){
    		errors{
                field
                messages
            }
            category{
                id
                name
            }    	
        }
    }
    mutation updateCategoryByFormInput($input: UpdateCategoryByFormInput!) {
        updateCategoryByForm(input: $input){
    		errors{
                field
                messages
            }
            category {
                id
                name
            }
        }
    }

    '''
