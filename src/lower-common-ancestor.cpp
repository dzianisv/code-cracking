/**
 * returns true if found
 */
bool findPath(Node* root, int key, std::list<Node*>& path) 
{
    if (!root) {
        return false;
    }
    
    path.push_back(root);
    
    if (root->data == key) {
        return true;
    }
    
    if (findPath(root->left, key, path) || findPath(root->right, key, path)) {
        return true;
    }

    path.pop_back();
    return false;
}

Node* lca(Node* root, int n1, int n2 )
{
    if (!root) {
        return nullptr;
    }
    
    std::list<Node*> path1, path2;
    
    if (!findPath(root, n1, path1) || !findPath(root, n2, path2)) {
        return nullptr;
    }
   
    Node* common = nullptr;
    
    auto&& i = path1.begin();
    auto&& j = path2.begin();
    
    for (; i != path1.end() && j != path2.end(); i++, j++) {
        if ((**i).data == (**j).data) {
            common = *i;
        } else {
        	break;
        }
    }
    
    return common;
 }
