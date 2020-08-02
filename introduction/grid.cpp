#include <bits/stdc++.h>
using namespace std;

bool visited[7][7];
string path;
int answer = 0;

void move(int r, int c, int steps)
{

    if (c == 0 && r == 6)

    {

        if (steps == 48)
        {

            answer += 1;
            return;
        }
        return;
    }

    //up

    if (r > -1 && r < 6 && visited[r + 1][c])
    {
        if (r > 0)
        {
            if (visited[r - 1][c])

            {
                if (c < 6 && c > 0 && visited[r][c + 1] == false && visited[r][c - 1] == false)
                {
                    return;
                }
            }
        }
        else
        {
            if (c < 6 && c > 0 && visited[r][c + 1] == false && visited[r][c - 1] == false)
            {
                return;
            }
        }
    }

    //down
    if (r < 7 && r > 0 && visited[r - 1][c])
    {
        if (r < 6)
        {
            if (visited[r + 1][c])
            {
                if (c < 6 && c > 0 && visited[r][c + 1] == false && visited[r][c - 1] == false)
                {
                    return;
                }
            }
        }
        else
        {
            if (c < 6 && c > 0 && visited[r][c + 1] == false && visited[r][c - 1] == false)
            {
                return;
            }
        }
    }
    //left
    if (c > -1 && c < 6 && visited[r][c + 1])
    {
        if (c > 0)
        {
            if (visited[r][c - 1])
            {
                if (r < 6 && r > 0 && visited[r + 1][c] == false && visited[r - 1][c] == false)
                {
                    return;
                }
            }
        }
        else
        {

            if (r < 6 && r > 0 && visited[r + 1][c] == false && visited[r - 1][c] == false)
            {
                return;
            }
        }
    }
    //right
    if (c < 7 && c > 0 && visited[r][c + 1])
    {
        if (c < 6)
        {
            if (visited[r][c + 1])
            {
                if (r < 6 && r > 0 && visited[r + 1][c] == false && visited[r - 1][c] == false)
                {
                    return;
                }
            }
        }
        else
        {

            if (r < 6 && r > 0 && visited[r + 1][c] == false && visited[r - 1][c] == false)
            {
                return;
            }
        }
    }

    visited[r][c] = 1;

    if (path[steps] == '?')
    {
        if (r > 0 && visited[r - 1][c] == false)
        {
            move(r - 1, c, steps + 1);
        }
        if (r < 6 && visited[r + 1][c] == false)
        {
            move(r + 1, c, steps + 1);
        }
        if (c > 0 && visited[r][c - 1] == false)
        {
            move(r, c - 1, steps + 1);
        }
        if (c < 6 && visited[r][c + 1] == false)
        {
            move(r, c + 1, steps + 1);
        }
    }
    else
    {
        if (path[steps] == 'U' && r > 0 && visited[r - 1][c] == false)
        {
            move(r - 1, c, steps + 1);
        }
        if (path[steps] == 'D' && r < 6 && visited[r + 1][c] == false)
        {
            move(r + 1, c, steps + 1);
        }
        if (path[steps] == 'L' && c > 0 && visited[r][c - 1] == false)
        {
            move(r, c - 1, steps + 1);
        }
        if (path[steps] == 'R' && c < 6 && visited[r][c + 1] == false)
        {
            move(r, c + 1, steps + 1);
        }
    }
    visited[r][c] = 0;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> path;
    move(0, 0, 0);
    cout << answer;

    return 0;
}
