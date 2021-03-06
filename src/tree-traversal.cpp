
// C program for different tree traversals
#include <iostream>
#include <stack>
using namespace std;

/* A binary tree node has data, pointer to left child
and a pointer to right child */
struct Node
{
    int data;
    struct Node *left, *right;
    Node(int data)
    {
        this->data = data;
        left = right = NULL;
    }
};

/* Given a binary tree, print its nodes according to the
"bottom-up" postorder traversal. */
void printPostorder(struct Node *node)
{
    if (node == NULL)
        return;

    // first recur on left subtree
    printPostorder(node->left);

    // then recur on right subtree
    printPostorder(node->right);

    // now deal with the node
    cout << node->data << " ";
}

/* Given a binary tree, print its nodes in inorder*/
void printInorder(struct Node *node)
{
    if (node == NULL)
        return;

    /* first recur on left child */
    printInorder(node->left);

    /* then print the data of node */
    cout << node->data << " ";

    /* now recur on right child */
    printInorder(node->right);
}

/* Given a binary tree, print its nodes in preorder*/
void printPreorder(struct Node *node)
{
    if (node == NULL)
        return;

    /* first print data of node */
    cout << node->data << " ";

    /* then recur on left sutree */
    printPreorder(node->left);

    /* now recur on right subtree */
    printPreorder(node->right);
}

void printPreorder2(Node *root)
{
    Node *node = root;
    bool visited = false;
    std::stack<Node *> stack;

    while (node)
    {
        if (!visited)
        {
            cout << node->data << ' ';
        }
        if (node->left && !visited)
        {
            stack.push(node);
            node = node->left;
        }
        else if (node->right)
        {
            node = node->right;
            visited = false;
        }
        else if (!stack.empty())
        {
            node = stack.top();
            visited = true;
            stack.pop();
        }
        else
        {
            break;
        }
    }

    cout << endl;
}

void printInOrder2(Node *root)
{
    Node *node = root;
    bool visited = false;
    std::stack<Node *> stack;

    while (node)
    {
        if (node->left && !visited)
        {
            stack.push(node);
            node = node->left;
        }
        else if (node->right)
        {
            node = node->right;
            visited = false;
        }
        else
        {
            cout << node->data << ' ';
            if (stack.empty())
            {
                break;
            }
            else
            {
                node = stack.top();
                visited = true;
                stack.pop();
            }
            cout << node->data << ' ';
        }
    }

    std::cout << endl;
}

void printPostorder2(Node *root)
{
    Node *node = root;
    bool visited = false;
    std::stack<Node *> stack;

    while (node)
    {
        if (node->left)
        {
            stack.push(node);
            node = node->left;
            visited = false;
        }
        else if (node->right)
        {
            stack.push(node);
            node = node->right;
            visited = true;
        }
        else
        {
            cout << node->data  << ' ';
            if (stack.empty()) {
                break;
            } else {
                node = stack.top();
                stack.pop();
            }
        }
    }
}

/* Driver program to test above functions*/
int main()
{
    struct Node *root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    root->left->right = new Node(5);

    cout << "\nPreorder traversal of binary tree is \n";
    printPreorder(root);

    cout << "\nInorder traversal of binary tree is \n";
    printInorder(root);

    cout << "\nPostorder traversal of binary tree is \n";
    printPostorder(root);

    cout << "\nPreorder cycle\n";
    printPreorder2(root);

    cout << "\nInorder cycle\n";
    printInOrder2(root);

    return 0;
}
