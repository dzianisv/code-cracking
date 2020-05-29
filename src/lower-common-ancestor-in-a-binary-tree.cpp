Node* lca(Node* root, int n1, int n2 )
{
    if (!root) {
        return nullptr;
    }
    
    // walk and find the n1
    for (Node *i = root; i != nullptr; ) {
        if (n1 < i->data && n2 < i->data) {
            i = i->left;
        } else if (n1 > i->data && n2 > i->data) {
            i = i->right;
        } else {
            return i;
        }
    }
   
    return nullptr;
}
